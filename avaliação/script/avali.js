document.addEventListener('DOMContentLoaded', () => {
  let selectedColor = null;

  document.querySelectorAll('.color-box').forEach(colorBox => {
    colorBox.addEventListener('click', () => {
      selectedColor = colorBox.style.backgroundColor;
      document.querySelectorAll('.color-box').forEach(box => {
        box.style.border = '2px solid #000'; 
      });
      colorBox.style.border = '2px solid black'; 
    });
  });

  document.querySelectorAll('.option').forEach(option => {
    const isCorrect = option.dataset.answer === option.closest('.image').querySelector('img').alt;
    if (isCorrect) {
      option.classList.add('correct');
    } else {
      option.classList.add('incorrect');
    }
  });

  document.querySelectorAll('.option').forEach(option => {
    option.addEventListener('click', () => {
      if (selectedColor && option.classList.contains('correct') && !option.classList.contains('selected')) {
        option.classList.add('selected');
        option.style.backgroundColor = selectedColor;
      }
    });
  });

  document.getElementById('submitBtn').addEventListener('click', () => {
    document.querySelectorAll('.option').forEach(option => {
      option.classList.remove('selected');
      option.style.backgroundColor = '';
    });

    selectedColor = null;
    document.querySelectorAll('.color-box').forEach(box => {
      box.style.border = '2px solid #000';
    });

    document.getElementById('nome').value = '';
    document.getElementById('data').value = '';

    alert('Dados resetados com sucesso!');
  });
});
