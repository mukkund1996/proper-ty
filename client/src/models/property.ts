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
}

export interface Building {
  id: number;
  building_class: BuildingClass;
  lot: Lot;
  usage: string;
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

export interface PropertyTableRow {
  id: number;
  fullAddress: string;
  classDescription: string;
  estimatedMarketValue: number;
  buildingArea: number;
  buildingUse: string;
}

export const extractPropertyTableData = ({
  id,
  estimated_market_value: marketValue,
  building,
  address,
}: Property): PropertyTableRow => {
  return {
    id,
    fullAddress: address.full_address,
    classDescription: building.building_class.description,
    estimatedMarketValue: marketValue,
    buildingArea: building.lot.building_area,
    buildingUse: building.usage,
  } as PropertyTableRow;
};
