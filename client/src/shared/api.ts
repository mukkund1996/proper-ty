import type { PropertyResponse } from '@/models/property';
import { fetchWithBasicAuth } from '@/shared/auth';
import { API_URL } from '@/shared/constants';

export const getProperties = async (pageCount: number, pageSize: number) => {
  const response = await fetchWithBasicAuth(
    `${API_URL}/properties?page=${pageCount}&page_size=${pageSize}`,
    'GET',
  );
  if (response.ok) {
    const data = await response.json();
    return data as PropertyResponse[];
  }

  return [] as PropertyResponse[];
};
