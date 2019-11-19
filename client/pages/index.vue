<template>
  <div class="index-container">
    <BookForm class="book-form" :on-submit="onSubmit" :form="form" />
    <BookList class="book-list" :on-delete="onDelete" :on-edit="onEdit" :books="books" />
  </div>
</template>

<script>
import BookList from '../components/BookList.vue'
import BookForm from '../components/BookForm.vue'
import api from '../api'

export default {
  name: 'Books',
  middleware: [ 'authenticated' ],
  components: {
    BookList,
    BookForm
  },
  async asyncData () {
    let books = []

    try {
      await api.books.list()
        .then(list => { books = list })
    } catch (error) {
      // eslint-disable-next-line
      console.log(error)
    }
    return { books }
  },
  data () {
    return {
      books: [],
      form: {
        method: 'post',
        fields: {
          title: '',
          author: ''
        },
        errors: {}
      }
    }
  },
  mounted () {

  },
  methods: {
    onSubmit (form) {
      if (this.form.method === 'post') {
        this.onCreate(form.fields)
      } else if (this.form.method === 'put') {
        this.onUpdate(form.fields)
      }
    },
    onCreate (data) {
      api.books.create(data)
        .then((res) => {
          this.books.push({
            ...data,
            id: res.id
          })
          this.resetForm()
        })
        .catch(error => {
          this.form.errors = error.response.data
        })
    },
    onUpdate (data) {
      api.books.update(data.id, data)
        .then(() => {
          const booksCopy = [...this.books]
          for (let i in this.books) {
            if (this.books[i].id === data.id) {
              booksCopy[i] = { ...data }
            }
          }
          this.books = booksCopy
          this.resetForm()
        })
    },
    onDelete (id) {
      api.books.remove(id)
        .then(() => {
          this.books = this.books.filter(
            book => book.id !== id)
        })
    },
    onEdit (id) {
      for (let i in this.books) {
        if (this.books[i].id === id) {
          this.form.fields = { ...this.books[i] }
        }
      }
      this.form.method = 'put'
    },
    resetForm () {
      for (let key in this.form.fields) {
        this.form.fields[key] = ''
      }
      this.form.method = 'post'
    }
  }
}
</script>

<style>
.index-container {
  margin: 0 auto;
  width: 500px;
  height: 400px;
}
.index-container > * {
  vertical-align: top;
}
.book-form {
  display: inline-block;
  width: 50%;
  height: 100%;
}
.book-list {
  display: inline-block;
  width: 50%;
  height: 100%;
  overflow-y: auto;
}
</style>
