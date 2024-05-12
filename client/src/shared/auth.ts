import { Buffer } from 'buffer';

export const createBasicAuthToken = (username: string, password: string) => {
  const token = `${username}:${password}`;
  const encodedToken = Buffer.from(token).toString('base64');
  return `Basic ${encodedToken}`;
};

export const getAuthKey = () => localStorage.getItem('authToken');
export const setAuthKey = (key: string) => localStorage.setItem('authToken', key);

export const fetchWithBasicAuth = async (
  url: string,
  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH',
  options?: RequestInit,
  body?: any,
  basicAuthToken?: string,
) => {
  let token = getAuthKey();
  if (basicAuthToken) {
    token = basicAuthToken;
  } else if (!token) {
    throw new Error('No token provided');
  }

  const headers = {
    ...options?.headers,
    Authorization: token,
    'Content-Type': 'application/json',
  };
  const requestOptions = {
    ...options,
    headers,
    method,
    body: JSON.stringify(body),
  };

  const response = await fetch(url, requestOptions);
  return response;
};
