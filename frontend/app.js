async function loadScene(sceneId) {
  const response = await fetch(`http://127.0.0.1:8000/api/scenes/${sceneId}`);

  const data = await response.json();

  renderScene(data);
}

function renderScene(data) {
  document.getElementById('scene-title').innerText = data.title;
  document.getElementById('scene-description').innerText = data.description;

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
