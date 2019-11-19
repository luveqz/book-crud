<template>
  <div class="signup-card">
    <form action="/api/auth-token" method="post" @submit.prevent="signup">
      <h1>SIGN UP</h1>

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

      <div v-if="errors.email" class="error-list">
        <ul>
          <li v-for="error in errors.email" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="fields.email" type="text" placeholder="Email">

      <div v-if="errors.password" class="error-list">
        <ul>
          <li v-for="error in errors.password" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="fields.password" type="password" placeholder="Password">

      <div v-if="errors.password2" class="error-list">
        <ul>
          <li v-for="error in errors.password2" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <input v-model="fields.password2" type="password" placeholder="Confirm password">

      <div v-if="errors.captcha" class="error-list">
        <ul>
          <li v-for="error in errors.captcha" :key="error">
            {{error}}
          </li>
        </ul>
      </div>
      <div class="captcha-container">
        <img :src="captcha.image" alt="Captcha">
        <div class="actions">
          <button type="button" @click="refreshCaptcha">
            <i class="fas fa-sync"></i>
          </button>
          <button type="button">
            <i class="fas fa-volume-up"></i>
          </button>
        </div>
      </div>
      <input v-model="fields.captcha" type="text" placeholder="Enter CAPTCHA">

      <input v-model="fields.captcha_key" type="hidden">

      <div class="actions">
        <button type="submit">Create Account</button>
      </div>
    </form>
  </div>
</template>

<script>
import api from '../api'

export default {
  name: 'Signup',
  async asyncData () {
    let captcha = {}

    await api.captcha.refresh()
      .then(res => { captcha = res })

    return {
      captcha: {
        image: captcha.image_url,
        audio: captcha.audio_url
      },
      fields: {
        captcha_key: captcha.key
      }
    }
  },
  data () {
    return {
      fields: {
        username: '',
        email: '',
        password: '',
        password2: '',
        captcha_key: '',
        captcha: ''
      },
      captcha: {
        image: '',
        audio: ''
      },
      errors: {}
    }
  },
  methods: {
    signup () {
      api.auth.signup({
        username: this.fields.username,
        email: this.fields.email,
        password: this.fields.password,
        password2: this.fields.password2,
        captcha_key: this.fields.captcha_key,
        captcha: this.fields.captcha
      })
        .then((res) => {
          this.$router.push('/')
        })
        .catch(res => {
          this.errors = res.response.data
        })
    },
    refreshCaptcha () {
      api.captcha.refresh()
        .then(res => {
          this.captcha.image = res.image_url
          this.captcha.audio = res.audio_url
          this.fields.captcha_key = res.key
        })
        .catch(res => {
          this.errors = res.response.data
        })
    }
  }
}
</script>

<style lang="css" scoped>
  .signup-card {
    max-width: 200px;
    padding: 40px;
    background-color: white;
    border-radius: 8px;
    margin: 0 auto;
    border: 1px solid #d3d5d8;
  }
  h1 {
    margin-top: 0px;
  }
  .captcha-container {
    margin: 15px 0 5px 0;
    height: 40px;
  }
  .captcha-container img {
    height: 100%;
    float: left;
    border-radius: 8px;
  }
  .captcha-container .actions {
    height: 100%;
    float: right;
  }
  .captcha-container button {
    height: 100%;
    margin-left: 5px;
    background-color: #dddddd;
  }
  .signup-card .actions {
    text-align: right;
  }
  .signup-card .actions p {
    margin-top: 10px;
  }
  .signup-card button[type=submit] {
    margin-top: 15px;
  }
</style>
