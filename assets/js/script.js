/// <reference path="helpers_brasa.js" />
'use strict';

requisicaoGet('get-plataformas/', function(plataformas) {
    $(plataformas).each(function(index, plataforma) {
        $('#plataformas-ls').append(
            `<div class='col card d-flex align-items-center justify-content-center'>
                <img src='${base_url('static/img/' + plataforma.nome)}.png' class="card-img-top card-logo">
                <h6 class='card-subtitle'>${plataforma.nome}</h6>
                <a href='${plataforma.link}'><button class='btn btn-light btn-outline-secondary'>Entrar</button></a>
            </div>`
        )
    })
})

requisicaoGet('get-ferramentas/', function(ferramentas) {
    $(ferramentas).each(function(index, ferramenta) {
        $('#ferramentas-ls').append(
            `<div class='col'>
                <img src='${base_url('static/img/' + ferramenta.nome)}.png'>
                <p>${ferramenta.nome}</p>
                <a href='${ferramenta.link}'><button class='btn btn-light btn-outline-secondary'>Entrar</button></a>
            </div>`
        )
    })
})