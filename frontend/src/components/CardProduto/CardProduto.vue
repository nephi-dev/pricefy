<script setup lang="ts">
import { PropType, ref } from "vue";
import { formatarValor } from "./utilitarios";
import type { LancamentoProduto, Produto } from "./tipos";

defineProps({
    produto: {
        type: Object as PropType<Produto>,
        default: null,
    },
});

const ver = ref<"caro" | "barato">("caro");
const lancamentos = ref<LancamentoProduto[]>([
    {
        id: 1,
        estabelecimentoDoLancamento: {
            id: 1,
            nome: "Loja 1",
        },
        valorDoProduto: 2.99,
    },
    {
        id: 2,
        estabelecimentoDoLancamento: {
            id: 2,
            nome: "Loja 2",
        },
        valorDoProduto: 4.99,
    },
    {
        id: 3,
        estabelecimentoDoLancamento: {
            id: 3,
            nome: "Loja 3",
        },
        valorDoProduto: 6.99,
    },
]); // ! Usando como exemplo !
const data = ref("19/03/2022");

function inverterOrdem() {
    ver.value = ver.value === "caro" ? "barato" : "caro";
    lancamentos.value = lancamentos.value.reverse();
}
</script>

<template>
    <div class="produto-card">
        <div class="produto-imagem-wrapper">
            <img
                class="produto-imagem"
                :src="produto.urlImagem"
                :alt="produto.nome"
            />
        </div>
        <div class="produto-lancamentos-wrapper">
            <h2 class="data-lancamentos">{{ data }}</h2>
            <ul class="produto-lancamentos">
                <li class="dados-lancamento" v-for="lancamento in lancamentos">
                    <div class="nome-estabelecimento-wrapper">
                        <span>{{
                            lancamento.estabelecimentoDoLancamento.nome
                        }}</span>
                    </div>
                    <div class="valor-produto-wrapper">
                        <span>{{
                            formatarValor(lancamento.valorDoProduto)
                        }}</span>
                    </div>
                </li>
                <li>
                    <button @click="inverterOrdem">
                        Ver mais {{ ver }} primeiro
                    </button>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.produto-card {
    display: flex;
    flex-direction: row;
}
.produto-imagem-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}
.produto-imagem {
    width: 160px;
    height: 160px;
}
.produto-lancamentos {
    list-style: none;
}
.dados-lancamento {
    display: flex;
    flex-direction: column;
    margin: 8px 0;
}
</style>
