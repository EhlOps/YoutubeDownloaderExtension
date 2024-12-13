document.getElementById("download")?.addEventListener("click", () => {
	chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
		const currentTab = tabs[0];
		if (currentTab && currentTab.url) {
			chrome.runtime.sendMessage({ action: "download", url: currentTab.url });
		} else {
			console.error("Error");
		}
	});
});
