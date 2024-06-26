/// <reference path="jquery.min.js" />
'use strict'; 
/**linhas de configuração acima, evite apagar. @author Brunoggdev*/

/* ----------------------------------------------------------------------
// ALGUMAS FUNÇÕES REQUEREM JQUERY E/OU BOOTSTRAP 5
---------------------------------------------------------------------- */


/**
 * Retorna a url do sistema concatenado com o caminho opcional
 * @param {string} caminho_opcional Caminho para ser concatenado a url base
 * @returns {string} Retorna a url do sistema concatenado com o caminho opcional
 * @author Bruno
*/
function base_url(caminho_opcional = '') {
    // tratando trailind slashes
    return (BASE_URL.endsWith('/') ? BASE_URL.slice(0, -1) : BASE_URL) + '/' + (caminho_opcional.startsWith('/') ? caminho_opcional.slice(1) : caminho_opcional);
}



/**
 * Permite que o metodo formatarBRL() seja chamado em qualquer string para formata-la em reais
 * @author Brunoggdev
*/
String.prototype.formatarBRL = function() {
    const formatado = this.replace(/,/g, '').replace(',', '.');
    const value = parseFloat(formatado);

    if (isNaN(value)) {
        throw new Error('String não parece ser um número válido.');
    }

    return value.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    });
};



/**
 * Converte data do formato yyyy-mm-dd para dd/mm/yyyy, ideal para o usuário.
 * @param {string} data
 * @returns {string} String com a data em formato dd/mm/yyyy
 * @author Bruno
*/
function paraDiaMesAno(data) {
    return data.split("-").reverse().join('/');
}



/**
 * Converte data do formato dd/mm/yyyy para yyyy-mm-dd, ideal para queries de banco de dados.
 * @param {string} data
 * @returns {string} String com a data em formato yyyy-mm-dd
 * @author Bruno
*/
function paraAnoMesDia(data) {
    return data.split("/").reverse().join('-');
}



/**
 * Guarda ou retorna uma variavel que pode ser acessada de qualquer lugar;
 * A variável é codificada e decodificada automaticamente em base64 para maior segurança.
 * Se o segundo parametro for informado, define o valor da variavel, 
 * senão, retorna o valor guardado na chave informada ou null caso não exista;
 * @param {string} chave A chave (nome) do valor que será guardado/resgatado
 * @param {any} valor O valor da chave; Se informado, define o valor recebido, se não, o valor guardado é retornado.
 * @returns {any} O valor guardado na chave ou `null` caso não exista. 
 * @author Brunoggdev
*/
function global(chave, valor = null) {
    if (valor === null) {
        return btoa(window.localStorage.getItem(chave))
    }
    
    window.localStorage.setItem(chave, atob(valor))

    return valor
}



/**
 * Atalho para atribuir um evento onchange evitando bug de duplo-evento
 * @param {string} seletor_jquery seletor de elemento tal qual jquery
 * @param {function(object):void} callback Funcao a ser executada no change
 * @author Brunoggdev
*/
function onChange(seletor_jquery, callback) {
    $(seletor_jquery).off('change').on('change', callback)
}



/**
 * Atalho para atribuir um evento onkeyup evitando bug de duplo-evento
 * @param {string} seletor_jquery seletor de elemento tal qual jquery
 * @param {function(object):void} callback Funcao a ser executada no keyup
 * @author Brunoggdev
*/
function onKeyup(seletor_jquery, callback) {
    $(seletor_jquery).off('keyup').on('keyup', callback)
}



/**
 * Atalho para atribuir um evento onclick evitando bug de duplo-evento
 * @param {string} seletor_jquery seletor de elemento tal qual jquery
 * @param {function(object):void} callback Funcao a ser executada no click
 * @author Brunoggdev
*/
function onClick(seletor_jquery, callback) {
    $(seletor_jquery).off('click').on('click', callback)
}



/**
 * Atalho para delegar um evento de um seletor para outro (útil para elementos gerados dinamicamente com javascript como tabelas etc)
 * @param {string} seletor_jquery_pai seletor jquery do elemento pai (ex: id da tabela)
 * @param {string} seletor_jquery_filho seletor jquery do elemento filho (ex: classe do botão na linha da tabela)
 * @param {function(object):void} callback Funcao a ser executada no click
 * @author Brunoggdev
*/
function delegarOnClick(seletor_jquery_pai, seletor_jquery_filho, callback) {
    $(seletor_jquery_pai).off('click', seletor_jquery_filho).on('click', seletor_jquery_filho, callback)
}



/**
 * Atalho para abrir uma modal rapidamente se já não estiver aberta e retornar sua instancia
 * @param {string} id_modal id da modal
 * @returns {object} Instancia da modal que foi aberta
 * @author Brunoggdev
*/
function modal(id_modal) {
    if (!id_modal.startsWith("#")) {
        id_modal = "#" + id_modal;
    }

    const modal = new bootstrap.Modal(id_modal)
    
    if(! $(id_modal).hasClass('show')){
        modal.show()
    }
    
    return modal
}



/**
 * Atalho para abrir a modal de alerta
 * @param {string} texto mensagem do corpo da modal (pode ser em formato html)
 * @param {function(object):void|false} fechar Funcao opcional quando fechar a modal
 * @author Brunoggdev
*/
function alertar(texto, fechar = () => {}) {
    $('#alerta-brasa-mensagem').html(texto)
    
    const alerta = modal('alerta-brasa')
    alerta.hide()

    $('#alerta-brasa').off('hidden.bs.modal').on('hidden.bs.modal', function() {
        fechar()
    })

    alerta.show()
}



/**
 * Atalho para abrir a modal de confirmação
 * @param {string} texto mensagem do corpo da modal (pode ser em formato html)
 * @param {function(object):void} callback Funcao a ser executada caso confirme
 * @param {function(object):void|false} cancelar Funcao opcional para caso cancelar
 * @author Brunoggdev
*/
function confirmar(texto, callback, cancelar = () => {}) {
    $('#confirmacao-brasa-texto').html(texto)

    const confirmacao = modal('confirmacao-brasa')
    confirmacao.hide()

    onClick('#confirmacao-brasa-confirmar', function() {
        callback()
        confirmacao.hide()
    })
    onClick('#confirmacao-brasa-cancelar', function() {
        cancelar()
        confirmacao.hide()
    })
}



/**
 * Atalho para uma requisicao get com Jquery
 * @param {string} endpoint url da requisicao
 * @param {(resultado: Array)}callback funcao a ser executada com o retorno
 * @author Brunoggdev
*/
function requisicaoGet(endpoint, callback){
    const fullEndpoint = endpoint.startsWith('https://')
    ? endpoint
    : BASE_URL + endpoint;

    $.get(fullEndpoint, callback)
}



/**
 * Atalho para uma requisicao post com Jquery
 * @param endpoint url da requisicao
 * @param dados corpo da requisicao
 * @param callback funcao a ser executada com o retorno
 * @author Brunoggdev
*/
function requisicaoPost(endpoint, dados, callback){
    const fullEndpoint = endpoint.startsWith('https://')
    ? endpoint
    : BASE_URL + endpoint;

    // tratando caso onde dados não foram informados e invés disso a callback foi informada
    if (typeof dados === 'function') {
        callback = dados;
        dados = null;
    }

    $.post(fullEndpoint, dados, callback)
}


/**
 * Aplica um debounce na callback informada com um timeout opcional (300ms padrão)
 * @author Brunoggdev
*/
function debounce(callback, timeout = 300){
    let timer;

    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { callback.apply(this, args); }, timeout);
    };
}




/**
 * Devolve um objeto com os elementos da linha clicada mapeados para a respectiva coluna
 * @param {string} elemento o elemento jquery clicado ($(this))
 * @author Brunoggdev
*/
function linhaParaObjeto(clickedElement) {
    const rowData = {};
    const columnNames = [];
    const specialChars = {
        'ç': 'c',
        'á': 'a',
        'ã': 'a',
        'é': 'e',
        'ê': 'e',
        'í': 'i',
        'ó': 'o',
        'ô': 'o',
        'ú': 'u',
      };
      
    // pegando e tratando nomes das colunas
    $(clickedElement).closest('table').find('thead th').each(function() {
        const columnName = $(this).text().toLowerCase().replace(/[^\w\s]/gi, match => specialChars[match] || match).replace('.', '').replace(' ', '_');
        columnNames.push(columnName);
    });

    // mapeando colunas e linhas no objeto
    $(clickedElement).closest('td').siblings('td:not(:last-child):not(:last-child)').each(function(index) {
      const columnName = columnNames[index];
      const columnValue = $(this).text();
      rowData[columnName] = columnValue;
    });
    
    return rowData;
}


/**
 * Converte um valor em centavos para reais
 * @param {number} centavos valor em centavos para ser convertido
 * @returns {number} valor convertido para reais
 * @author Brunoggdev
*/
function paraReais(centavos) {
    return (centavos / 100).toLocaleString('pt-br',
    { minimumFractionDigits: 2, maximumFractionDigits: 2 }); // Returns the result with 2 decimal places
}


/**
 * Converte um valor em reais para centavos
 * @param {number} reais valor em reais para ser convertido
 * @returns {number} valor convertido para centavos
 * @author Brunoggdev
*/
function paraCentavos(reais) {
    return (parseFloat(reais.replace(',', '.')) * 100)
}

function cr7(csrf) {
    return csrf.siblings('[name="csrfmiddlewaretoken"]').attr('value')
}