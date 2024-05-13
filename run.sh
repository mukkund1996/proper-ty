touch client/.env.production
echo VITE_API_URL="http://localhost:8000/api" >> client/.env.production
echo VITE_MAPLIBRE_TOKEN="YOURTOKEN" >> client/.env.production

docker-compose up -d