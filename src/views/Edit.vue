<script lang="ts">
import { onBeforeMount, ref } from 'vue'
export default {
  props: {
    name: String
  },
  setup (props : any) {
    const article = ref('')
    onBeforeMount(async () => {
      const res: Response = await fetch('http://localhost:8000/articles/' + props.name, {
        method: 'GET',
        headers: {
          Accept: 'application/json'
        }
      })
      article.value = await res.text()
    })

    async function save () {
      const res: Response = await fetch('http://localhost:8000/articles/' + props.name, {
        method: 'PUT',
        headers: {
          Accept: 'application/json'
        },
        body: article.value
      })
    }
    return {
      article,
      save
    }
  }
}
</script>

<template>
<div>
<button class="btn"><router-link to="/">Home</router-link></button>
<h3 id="article">{{ name.toUpperCase() }}</h3>

<textarea id="input-desc" class="desc" v-model="article" rows="4"></textarea>
<p id="preview" class="desc">{{ article}}</p>

<button class="btn"><router-link :to="{path:'/'+article, name: 'Article', params: { name: name } }">Cancel</router-link></button>
<button class="btn" @click="save()"><router-link :to="{path:'/', name: 'Home', params: { name: name } }">Save</router-link></button>
</div>
</template>

<style>
.btn {
margin-right: 20px;
}
textarea {
width: 400px;
height: 100px;
}
</style>
