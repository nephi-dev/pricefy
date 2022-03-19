<script setup lang="ts">
import CardProduto from "../components/CardProduto/CardProduto.vue";
const produtoQualquer = {
    id: 1,
    nome: "Tomate",
    urlImagem:
        "https://www.infoescola.com/wp-content/uploads/2011/01/tomate_345187874.jpg",
};
</script>

<template>
    <h1>Inicio do Pricefy</h1>
    <CardProduto :produto="produtoQualquer" />
    <CardProduto :produto="produtoQualquer" />
    <CardProduto :produto="produtoQualquer" />
    <CardProduto :produto="produtoQualquer" />
</template>

<style scoped></style>
