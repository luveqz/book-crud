<template>
  <div>
    <article class="book-card" v-for="book in books" :key="book.id" id="">
      <p class="title">{{book.title}}</p>
      <p class="author">{{book.author}}</p>
      <div class="actions">
        <button @click="() => callOnDelete(book.id)" class="btn-remove">Delete</button>
        <button @click="() => callOnEdit(book.id)" class="btn-edit">Edit</button>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: 'BookList',
  props: {
    books: {
      type: Array,
      required: true
    },
    onDelete: {
      type: Function,
      required: true
    },
    onEdit: {
      type: Function,
      required: true
    }
  },
  methods: {
    callOnDelete (id) {
      this.onDelete(id)
    },
    callOnEdit (id) {
      this.onEdit(id)
    }
  }
}
</script>

<style lang="css">
  .book-card {
    width: 88%;
    padding: 5%;
    background-color: white;
    border-radius: 8px;
    margin-bottom: 10px;
    border: 1px solid #d3d5d8
  }
  .book-card p {
    margin: 0px;
  }
  .title {
    font-weight: bold;
  }
  .author {
    font-size: 14px;
  }
  .book-card .actions {
    margin-top: 5px;
    text-align: right;
  }
  .book-card button {
    margin-left: 5px;
  }
  .btn-remove {
    border-radius: 8px;
    cursor: pointer;
    border: none;
    padding: 5px 10px;
    background-color: #ec226e;
    color: white;
  }
  .btn-remove:hover {
    background-color: #f95995;
  }
  .btn-edit {
    border-radius: 8px;
    cursor: pointer;
    border: none;
    padding: 5px 10px;
    background-color: #ecb322;
    color: white;
  }
  .btn-edit:hover {
    background-color: #f4c242;
  }
</style>
