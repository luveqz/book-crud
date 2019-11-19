<template>
  <nav>
    <div class="center">
      <ul>
        <li v-if="$store.state.auth">
          <nuxt-link exact to="/">Dashboard</nuxt-link>
        </li>
      </ul>
      <ul>
        <li v-if="!$store.state.auth">
          <nuxt-link to="/signup">Sign up</nuxt-link>
        </li>
        <li v-if="!$store.state.auth" class="btn-login">
          <nuxt-link to="/login">Login</nuxt-link>
        </li>
        <li v-if="$store.state.auth" class="btn-login">
          <a href="#" @click="logout">Logout</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
const Cookie = process.client ? require('js-cookie') : undefined

export default {
  name: 'Navbar',
  methods: {
    logout () {
      Cookie.remove('auth')

      this.$store.commit('setAuth', null)

      this.$router.push('/login')
    }
  }
}
</script>

<style>
  .container .center {
    max-width: 800px;
    margin: 0 auto;
  }
  .container nav ul:first-child {
    text-align: left;
  }
  .container nav ul:last-child {
    text-align: right;
  }
  .container nav {
    text-align: right;
    background-color: #1e242c;
    width: 100%;
    margin-bottom: 20px;
  }
  .container nav ul {
    width: 50%;
    margin: 0px;
    padding: 0px;
    display: inline-block;
  }
  .container nav li {
    list-style: none;
    display: inline-block;
  }
  .container nav a:hover,
  .container nav a:focus {
    background-color: #2e3742;
  }
  .container nav a {
    padding: 10px 20px;
    display: block;
    text-decoration: none;
    color: white;
    border-top: 4px solid transparent;
    border-bottom: 4px solid transparent;
    outline: none;
  }
  .container nav a.active {
    border-bottom-color: #98b2cc;
    color: #98b2cc;
  }

</style>
