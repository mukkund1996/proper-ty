export type SearchKey = 'address' | 'class' | 'marketValue' | 'area' | 'usage';

export type SearchKeyValue = {
  key: SearchKey;
  value: string;
};
