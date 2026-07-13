import axios from 'axios';
const baseUrl = import.meta.env.VITE_API_BASE_URL;

const service = axios.create({
  baseURL: baseUrl,
  timeout: 6000,
});

export default service;
