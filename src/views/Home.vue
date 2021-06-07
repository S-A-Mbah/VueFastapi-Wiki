<script lang="ts">
import { onBeforeMount, ref } from 'vue'
export default {
  setup () {
    const articles = ref([])
    onBeforeMount(async () => {
      // eslint-disable-next-line

      const res: Response = await fetch('http://localhost:8000/articles/', {
        method: 'GET',
        headers: {
          Accept: 'application/json'
        }
      })
      articles.value = await res.json()
    })
    return {
      articles
    }
  }
}
</script>

<template>
  <div>
    <button class="btn"><router-link to="/">Home</router-link></button>

    <h3>ARTICLES</h3>
    <p v-if="loading" class="post--empty">Loading....</p>
    <div v-else class="article" v-for="article in articles" :key="article">
      <button class="btn">
        <router-link :to="{ path:'/'+article.name, params: { name: article } }">{{
          article
        }}</router-link>
      </button>
    </div>
  </div>
</template>

<style>
.btn {
  margin-right: 20px;
}
</style>
