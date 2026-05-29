async function submitQuiz() {

    const username = document.getElementById("username").value;

    const family = document.getElementById("family").value;

    const occasion = document.getElementById("occasion").value;

    const intensity = document.getElementById("intensity").value;
    
    const gender = document.getElementById("gender").value;

    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = `
        <p class="text-muted">
            Generando recomendaciones...
        </p>
    `;

    try {

        const response = await fetch("/quiz-recommend", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                family,
                occasion,
                intensity,
                gender
            })
        });

        const data = await response.json();

        resultsDiv.innerHTML = "";

        if (data.length === 0) {

            resultsDiv.innerHTML = `

                <div class="alert alert-warning">

                    No encontramos perfumes compatibles.

                </div>

            `;

            return;
        }

        data.forEach(perfume => {

            resultsDiv.innerHTML += `

            <div class="card shadow-sm mb-4 border-0">

                <div class="row g-0">

                    <div class="col-md-4 d-flex align-items-center">

                        <img
                            src="${perfume.imagen}"
                            class="img-fluid rounded-start"
                            alt="${perfume.perfume}"
                            style="
                                height: 100%;
                                object-fit: cover;
                            "
                        >

                    </div>

                    <div class="col-md-8">

                        <div class="card-body">

                            <h4 class="card-title">
                                ${perfume.perfume}
                            </h4>

                            <p class="text-muted mb-2">
                                ${perfume.marca}
                            </p>

                            <p class="mb-1">
                                Intensidad:
                                <strong>${perfume.intensidad}</strong>
                            </p>

                            <p class="mb-1">
                                Precio:
                                <strong>Q${perfume.precio}</strong>
                            </p>

                            ${
                                perfume.score
                                ?
                                `
                                <p class="mb-0">
                                    Score:
                                    <strong>${perfume.score.toFixed(2)}</strong>
                                </p>
                                `
                                :
                                ''
                            }

                        </div>

                    </div>

                </div>

            </div>

            `;
        });

    } catch (error) {

        console.error(error);

        resultsDiv.innerHTML = `

            <div class="alert alert-danger">

                Error obteniendo recomendaciones.

            </div>

        `;
    }
}