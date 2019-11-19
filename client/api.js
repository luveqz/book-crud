import axios from 'axios'

const Cookie = process.client ? require('js-cookie') : undefined

const HOST = process.client ? window.location.hostname : 'django:8000'
const SCHEME = process.client ? location.protocol : 'http:'
const BASE_URL = `${SCHEME}//${HOST}/api`

// const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
// const randomNumber = (min = 0, max = 1) =>
//   Math.floor(Math.random() * (max - min + 1)) + min
// const simulateNetworkLatency = (min = 30, max = 1500) =>
//   delay(randomNumber(min, max))

async function callAPI (endpoint, options = {}) {
  // await simulateNetworkLatency()

  options.headers = {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  }

  try {
    let auth = Cookie.get('auth')
    let parsed = JSON.parse(auth)
    let headerValue = `Token ${parsed.accessToken}`
    options.headers.Authorization = headerValue
  } catch (err) {
    // No valid cookie found
  }

  const url = BASE_URL + endpoint
  const response = await axios({ url, ...options })

  return response.data
}

const api = {
  books: {
    list () {
      return callAPI('/books/')
    },
    create (book) {
      // throw new Error('500: Server error');
      return callAPI(`/books/`, {
        method: 'POST',
        data: book
      })
    },
    read (bookId) {
      return callAPI(`/books/${bookId}/`)
    },
    update (bookId, updates) {
      return callAPI(`/books/${bookId}/`, {
        method: 'PUT',
        data: updates
      })
    },
    remove (bookId) {
      return callAPI(`/books/${bookId}/`, {
        method: 'DELETE'
      })
    }
  },

  auth: {
    signin (credentials) {
      return callAPI('/auth/get-token', {
        method: 'POST',
        data: credentials
      })
    },
    signup (data) {
      return callAPI('/auth/signup', {
        method: 'POST',
        data
      })
    }
  },

  captcha: {
    refresh () {
      return callAPI('/captcha/refresh', {
        method: 'GET'
      })
    }
  }
}

export default api
