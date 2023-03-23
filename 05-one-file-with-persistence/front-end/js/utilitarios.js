/*
 
            FUNÇÃO UTILITÁRIA
 
            */

            function encontrarErro(jqXHR, textStatus, rota) {
                var msg = '';
                if (jqXHR.status === 0) {
                    msg = 'Não foi possível conectar, ' +
                        'verifique se o endereço do backend está certo' +
                        ' e se o backend está rodando.';
                } else if (jqXHR.status == 404) {
                    msg = 'A URL informada não foi encontrada no ' +
                        'servidor [erro 404]: ' + rota;
                } else if (jqXHR.status == 500) {
                    msg = 'Erro interno do servidor [erro 500], ' +
                        'verifique nos logs do servidor';
                } else if (textStatus === 'parsererror') {
                    msg = 'Falha ao decodificar o resultado json';
                } else if (textStatus === 'timeout') {
                    msg = 'Tempo excessivo de conexão, estourou o limite (timeout)';
                } else if (textStatus === 'abort') {
                    msg = 'Requisição abortada (abort)';
                } else {
                    msg = 'Erro desconhecido: ' + jqXHR.responseText;
                }
                return msg;
            }