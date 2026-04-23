document.addEventListener('DOMContentLoaded', () => {
    const downloadBtn = document.getElementById('downloadBtn');

    if (downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            console.log('Download initiated for CurvySnake.py');
            // Adding a simple visual feedback for the user
            downloadBtn.innerText = "Downloading...";
            setTimeout(() => {
                downloadBtn.innerText = "Download Game (.py)";
            }, 2000);
        });
    }
});
