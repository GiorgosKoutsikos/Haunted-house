let currentSanity = 100;

async function loadScene(sceneId) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/scenes/${sceneId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    renderScene(data);
  } catch (error) {
    console.error('Failed to load scene:', error);
    document.getElementById('scene-title').innerText = 'Connection Error';
    document.getElementById('scene-description').innerText =
      'Cannot connect with server';
  }
}

function renderScene(data) {
  document.getElementById('scene-title').innerText = data.title;
  document.getElementById('scene-description').innerText = data.description;

  currentSanity += data.sanity_impact;
  if (currentSanity <= 0) currentSanity = 0;
  document.getElementById('sanity-value').innerText = currentSanity;

  const container = document.getElementById('choices-container');
  container.innerHTML = '';

  function createRestartButton(buttonText) {
    const restartBtn = document.createElement('button');
    restartBtn.className = 'choice-btn';
    restartBtn.innerText = buttonText;
    restartBtn.addEventListener('click', () => {
      currentSanity = 100;
      document.getElementById('sanity-value').innerText = currentSanity;
      loadScene(1);
    });
    container.appendChild(restartBtn);
  }

  if (currentSanity === 0) {
    document.getElementById('scene-title').innerText = 'Gamer Over';
    document.getElementById('scene-description').innerText =
      'You lost your mind in the dark';
    createRestartButton('Try Again');
  } else if (data.choices.length === 0) {
    createRestartButton('Play Again');
  } else {
    data.choices.forEach((choice) => {
      const button = document.createElement('button');
      button.className = 'choice-btn';
      button.innerText = choice.choice_text;

      button.addEventListener('click', () => {
        loadScene(choice.target_scene_id);
      });
      container.appendChild(button);
    });
  }
}

loadScene(1);
