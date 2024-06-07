import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import api from "../api";

function Country() {
  const params = useParams();
  const [countries, setCountries] = useState([]);

  useEffect(() => {
    getCountries();
  }, []);

  const getCountries = () => {
    api
      .get("/api/countries/")
      .then((res) => res.data)
      .then((data) => {
        const normalizedData = data.map((country) => ({
          ...country,
          name: decodeURIComponent(country.name.replace(/_/g, " ")),
          popular_cities: country.popular_cities
            .replace("[", "")
            .replace("]", "")
            .replace(/"/g, "")
            .replace(/_/g, " "),
        }));
        setCountries(normalizedData);
      })
      .catch((err) => alert(err));
  };

  const filteredCountry = countries.filter(
    (value) => value.name.toLowerCase() === params.countryName.toLowerCase()
  );

  const result = filteredCountry.map((country) => (
    <div key={country.id}>
      {country.popular_cities.split(",").map((city, index) => (
        <p key={index}>{decodeURI(city)}</p>
      ))}
    </div>
  ));

  return (
    <div>
      <h1>{params.countryName}</h1>

      {result}
    </div>
  );
}

export default Country;
