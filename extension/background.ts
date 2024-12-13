chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
	if (message.action === "download" && message.url) {
		fetch("http://localhost:8888/yt-dl", {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ url: message.url }),
		})
			.then((response) => {
				console.log(response);
				sendResponse(response);
			})
			.catch((error) => {
				console.error(error);
				sendResponse({ error: error });
			});
		return true;
	}
});
