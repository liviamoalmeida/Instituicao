// Garantir que o script funcione apenas depois que o DOM estiver completamente carregado
document.addEventListener('DOMContentLoaded', () => {
    // Seleciona todos os mini players
    const miniPlayers = document.querySelectorAll('.thumbnail-video');
  
    // Seleciona o iframe do vídeo principal
    const mainVideo = document.getElementById('main-video');
  
    // Adiciona o evento de clique para cada mini player
    miniPlayers.forEach(player => {
      player.addEventListener('click', function () {
        // Pega o src do mini player clicado
        const newSrc = player.getAttribute('src');
        
        // Atualiza o src do vídeo principal
        mainVideo.src = newSrc.replace('embed/', 'embed/'); // Evitar duplicação do 'embed/' no link
      });
    });
  });
  