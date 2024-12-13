"use strict";
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "download" && message.url) {
        fetch(message.url)
            .then((response) => {
            console.log(response);
        })
            .catch((error) => {
            console.error(error);
        });
    }
});
