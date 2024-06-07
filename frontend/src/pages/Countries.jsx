import { useState, useEffect } from "react";
import api from "../api";

function Countries() {
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
          name: decodeURI(country.name.replace(/_/g, " ")),
        }));
        setCountries(normalizedData);
        console.log(normalizedData);
      })
      .catch((err) => alert(err));
  };
  return (
    <div>
      <h2>Countries</h2>
      {countries.length > 0 ? (
        <ul>
          {countries.map((country) => (
            <li key={country.id}>{country.name}</li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Countries;
