async function getRecommendations() {

    const username = document.getElementById("username").value;

    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = `
        <p class="text-muted">
            Buscando recomendaciones...
        </p>
    `;

    try {

        const response = await fetch("/recommend", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username
            })
        });

        const data = await response.json();

        resultsDiv.innerHTML = "";


        if (data.length === 0) {

            resultsDiv.innerHTML = `

                <div class="alert alert-warning mt-4">

                    No se encontraron recomendaciones para este usuario.

                </div>

            `;

            return;
        }


        data.forEach(perfume => {

            resultsDiv.innerHTML += `

                <div class="card shadow-sm mb-4 border-0">

                    <div class="row g-0">

                        <div class="col-md-4">

                            <img
                                src="${
                                    perfume.imagen &&
                                    perfume.imagen !== ''
                                    ?
                                    perfume.imagen
                                    :
                                    'https://via.placeholder.com/300x300?text=Perfume'
                                }"

                                class="img-fluid rounded-start"

                                alt="${
                                    perfume.perfume || 'Perfume'
                                }"

                                style="
                                    height: 100%;
                                    object-fit: cover;
                                "
                            >

                        </div>

                        <div class="col-md-8">

                            <div class="card-body">

                                <h4 class="card-title">
                                    ${
                                        perfume.perfume || 'Perfume sin nombre'
                                    }
                                </h4>

                                <p class="text-muted mb-2">

                                    ${
                                        perfume.marca || 'Marca desconocida'
                                    }

                                </p>

                                <p class="mb-1">

                                    Intensidad:

                                    <strong>

                                        ${
                                            perfume.intensidad || 'No especificada'
                                        }

                                    </strong>

                                </p>

                                <p class="mb-1">

                                    Precio:

                                    <strong>

                                        ${
                                            perfume.precio
                                            ?
                                            'Q' + perfume.precio
                                            :
                                            'No disponible'
                                        }

                                    </strong>

                                </p>

                                ${
                                    perfume.score !== undefined
                                    ?

                                    `
                                    <p class="mb-0">

                                        Score:

                                        <strong>

                                            ${Number(perfume.score).toFixed(2)}

                                        </strong>

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

            <div class="alert alert-danger mt-4">

                Ocurrió un error obteniendo recomendaciones.

            </div>

        `;
    }
}