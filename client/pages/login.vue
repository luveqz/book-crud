<template>
  <div class="signin-card">
    <form action="/api/auth-token" method="post" @submit.prevent="signin">
      <h1>LOGIN</h1>

      <div v-if="errors.non_field_errors" class="error-list non-field-errors">
        <ul>
          <li v-for="error in errors.non_field_errors" :key="error">
            {{error}}
          </li>
        </ul>
      </div>

      <div v-if="errors.username" class="error-list">
        <ul>
          <li v-for="error in errors.username" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="fields.username" type="text" placeholder="Username">

      <div v-if="errors.password" class="error-list">
        <ul>
          <li v-for="error in errors.password" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="fields.password" type="password" placeholder="Password">

      <div class="actions">
        <button type="submit">Login</button>
        <p>
          Need an account?<br>
          <nuxt-link to="/signup">Register</nuxt-link>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import api from '../api'

const Cookie = process.client ? require('js-cookie') : undefined

export default {
  name: 'Signin',
  data () {
    return {
      fields: {
        username: '',
        password: ''
      },
      errors: {}
    }
  },
  methods: {
    signin () {
      api.auth.signin({
        username: this.fields.username,
        password: this.fields.password
      })
        .then((res) => {
          const auth = { accessToken: res.token }

          // mutating to store for client rendering
          this.$store.commit('setAuth', auth)

          // saving token in cookie for server rendering
          Cookie.set('auth', auth)

          this.$router.push('/')
        })
        .catch(error => {
          this.errors = error.response.data
        })
    }
  }
}
</script>

<style lang="css" scoped>
  .signin-card {
    max-width: 200px;
    padding: 40px;
    background-color: white;
    border-radius: 8px;
    margin: 0 auto;
    border: 1px solid #d3d5d8
  }
  h1 {
    margin-top: 0px;
  }
  .actions {
    text-align: right;
  }
  .actions p {
    margin-top: 10px;
  }
</style>
