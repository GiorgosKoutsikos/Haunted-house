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
  document.getElementById('sanity-value').innerText = currentSanity;

  const container = document.getElementById('choices-container');
  container.innerHTML = '';

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

loadScene(1);
