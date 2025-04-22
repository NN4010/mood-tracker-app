document.getElementById('moodForm').addEventListener('submit', async function(event) {
  event.preventDefault();
  
  const mood = document.getElementById('mood').value;
  const note = document.getElementById('note').value;

  const response = await fetch('https://your-backend-url.onrender.com/save_mood', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mood, note })
  });

  if (response.ok) {
    alert('Mood Saved Successfully!');
    loadMoods();
    document.getElementById('moodForm').reset();
  }
});

async function loadMoods() {
  const response = await fetch('https://your-backend-url.onrender.com/get_moods');
  const data = await response.json();

  const list = document.getElementById('moodList');
  list.innerHTML = '';

  data.moods.forEach(entry => {
    const item = document.createElement('li');
    item.textContent = `${entry.date} - ${entry.mood}: ${entry.note || ''}`;
    list.appendChild(item);
  });
}

window.onload = loadMoods;
