const player = document.getElementById('m3u8-player');
const episodeSelect = document.getElementById('episode-select');

function loadEpisode() {
    const selectedEpisode = episodeSelect.value;
    if (selectedEpisode) {
        player.src = selectedEpisode;
        player.play();
    }
}

episodeSelect.addEventListener('change', loadEpisode);