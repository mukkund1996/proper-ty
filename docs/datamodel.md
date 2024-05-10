## Datamodel

```mermaid
erDiagram
    Property {
      int id PK
      Sale sale FK
      Building building FK
      Address address FK
      Location location FK
      float estimated_market_value
      int full_bath_count
      int half_bath_count
      boolean fireplace
      string garage_description
    }
    Address ||--|| Property : locates
    Location ||--|| Property : locates
    Building ||--|{ Property : contains
    Sale }o--|| Property : describes

    Location {
      int id PK
      Address address FK
      float latitude
      float longitude
    }

    Location ||--|{ Address : contains

    Address {
      int id PK
      int tax_code
      int neighbourhood
      int house_num
      int dir
      string street
      string suffix
      string city
      int zip
    }
    
    Building {
      int id PK
      Class class FK
      Lot lot
      string type
      string usage
      int apartment_count
      int commercial_unit_count
      string external_description
      string basement_description
      string attic_description
      int ac_count
      int age
      int unit_count
      boolean multi_sale
    }
    Class {
      int id PK
      string description
      int class_number
    }
    Class ||--|{ Building : describes 
    Lot ||--o{ Building : contains

    Sale {
      int id PK
      float amount
      float date
      int deed_type
    }

    Lot {
      int id PK
      float current_land_area
      float current_building_area
      float current_total_area
      float prior_land_area
      float prior_building_area
      float prior_total_area
    }

    User {
      int id PK
      string first_name
      string last_name
      string username
      string password_token
    }

    User_Property_Relation {
      int id PK 
      User user FK
      Property property FK
    }

    User }o--|| User_Property_Relation : favourites
    User_Property_Relation ||--o{ Property : links

```