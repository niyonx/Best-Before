import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchResource () {
    return $axios.get(`resource/xxx`)
      .then(response => response.data)
  },

  fetchSecureResource () {
    return $axios.get(`secure-resource/zzz`)
      .then(response => response.data)
  },

  getProducts () {
    return $axios.get(`getProducts`)
      .then(response => response.data)
  },

  checkUser (username = '', password = '') {
    return $axios.get('checkUser/' + username + '/' + password)
      .then(response => response.data)
  },

  createUser (username = '', password = '', phone = '') {
    return $axios.get('createUser/' + username + '/' + password + '/' + phone)
      .then(response => response.data)
  },

  createProduct (product_name = '', product_brand = '', expiry_date = '', user_id = '') {
    return $axios.get('createProduct/' + product_name + '/' + product_brand + '/' + expiry_date + '/' + user_id)
      .then(response => response.data)
  },

  deleteProduct (product_id = '') {
    return $axios.get('deleteProduct/' + product_id)
      .then(response => response.data)
  },

  totalProducts () {
    return $axios.get('totalProducts/')
      .then(response => response.data)
  }

}
