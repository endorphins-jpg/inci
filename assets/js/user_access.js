/// <reference path="helpers_brasa.js" />
'use strict';

requisicaoGet('user-access/', function(access) {
    let plataformas = access.plataformas
    let ferramentas = access.ferramentas

    $(plataformas).each(function(index, plataforma) {
        $('#plataformas-ls').append(
            `<div class='card d-flex mb-3 me-3 justify-content-center p-3'>
                <div class='d-flex flex-column align-items-center my-4'>
                    <img src='${base_url('static/img/icons/' + plataforma.nome)}.png' class="card-img-top card-logo">
                    <h6 class='card-subtitle mt-1'>${plataforma.nome}</h6>
                </div>
                <a href='${plataforma.link}'>
                    <button class='btn btn-inci-neutral w-100'>Entrar</button>
                </a>
            </div>`
        )
    })

    $(ferramentas).each(function(index, ferramenta) {
        $('#ferramentas-ls').append(
            `<div class='card d-flex mb-3 me-3 justify-content-center p-3'>
                <div class='d-flex flex-column align-items-center my-4'>
                    <img src='${base_url('static/img/icons/' + ferramenta.nome)}.png' class="card-img-top card-logo">
                    <h6 class='card-subtitle mt-1'>${ferramenta.nome}</h6>
                </div>
                <a href='${ferramenta.link}'>
                    <button class='btn btn-inci-neutral w-100'>Entrar</button>
                </a>
            </div>`
        )
    })
})
