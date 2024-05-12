import type { PropertyResponse } from '@/models/property';
import { fetchWithBasicAuth } from '@/shared/auth';
import { API_URL } from '@/shared/constants';
import type { SearchKeyValue } from './types';

export const getProperties = async (limit: number, searchKeyValue?: SearchKeyValue) => {
  const requestUrl = `${API_URL}/properties?limit=${limit}${searchKeyValue ? `&search_key=${searchKeyValue.key}&search_value=${searchKeyValue.value}` : ''}`;
  const response = await fetchWithBasicAuth(requestUrl, 'GET');
  if (response.ok) {
    const data = await response.json();
    return data as PropertyResponse;
  }

  return null;
};
