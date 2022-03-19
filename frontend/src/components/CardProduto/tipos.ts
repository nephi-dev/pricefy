export type LancamentoProduto = {
    id: number;
    valorDoProduto: number;
    estabelecimentoDoLancamento: {
        id: number;
        nome: string;
    };
};

export type Produto = {
    id: number;
    nome: string;
    urlImagem: string;
};
