interface Address {
  id: number;
  full_address: string;
}

export interface Location {
  id: number;
  latitude: number;
  longitude: number;
}

export interface BuildingClass {
  id: number;
  description: string;
}

export interface Lot {
  id: number;
  building_area: number;
  land_area: number;
}

export interface Building {
  id: number;
  building_class: BuildingClass;
  lot: Lot;
}

export interface Property {
  id: number;
  estimated_market_value: number;
  building: Building;
  address: Address;
  location: Location;
}

export interface PropertyResponse {
  properties: Property[];
  totalCount: number;
  totalPages: number;
  countPerPage: number;
}
