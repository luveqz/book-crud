<template>
  <div>
    <form action="/books" :method="form.method" @submit.prevent="callOnSubmit">
      <h1 v-if="form.method == 'post'">NEW BOOK</h1>
      <h1 v-else-if="form.method == 'put'">EDIT BOOK</h1>

      <input v-model="form.fields.id" type="hidden" name="id">

      <div v-if="form.errors.title" class="error-list">
        <ul>
          <li v-for="error in form.errors.title" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="form.fields.title" type="text"
             name="title" placeholder="Title">

      <div v-if="form.errors.author" class="error-list">
        <ul>
          <li v-for="error in form.errors.author" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="form.fields.author" type="text"
             name="author" placeholder="Author">

      <button v-if="form.method == 'post'" type="submit" name="submit">Create</button>
      <button v-if="form.method == 'put'" type="submit" name="submit">Update</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'book-form',
  props: {
    form: {
      type: Object,
      required: true
    },
    onSubmit: {
      type: Function,
      required: true
    }
  },
  methods: {
    callOnSubmit () {
      this.onSubmit(this.form)
    }
  }
}
</script>

<style lang="css" scoped>
  h1 {
    margin-top: 0px;
  }
  form {
    background-color: white;
    width: 73%;
    padding: 10%;
    margin-right: 5%;
    border: 1px solid #d3d5d8;
    border-radius: 8px;
  }
</style>
