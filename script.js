fetch('news.json')
  .then(res => res.json())
  .then(data => {
    let container = document.getElementById("news");

    data.forEach(article => {
      container.innerHTML += `
        <div class="card">
          <img src="${article.image}">
          <h2>${article.title}</h2>
          <p>${article.summary}</p>
          <a href="${article.link}" target="_blank">Read Full</a>
        </div>
      `;
    });
  });
