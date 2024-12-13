"use strict";
var _a;
(_a = document.getElementById("download")) === null || _a === void 0 ? void 0 : _a.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentTab = tabs[0];
        if (currentTab && currentTab.url) {
            chrome.runtime.sendMessage({ action: "download", url: currentTab.url });
        }
        else {
            console.error("Error");
        }
    });
});
