chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
	if (message.action === "download" && message.url) {
		fetch("http://localhost:8888/yt-dl", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ url: message.url }),
		})
			.then((response) => {
				response.json().then((data) => {
					const result = data.message;
					console.log(result);
					sendResponse(result);
				});
			})
			.catch((error) => {
				console.error(error);
				sendResponse({ error: error });
			});
		return true;
	}
});
