import axios from "axios";

// Fetch companies by state
export const getCompaniesByState = async (stateCode) => {
    try {
        const response = await axios.get(
            `http://localhost:8080/v1/company/state/${stateCode}`
        );
        return response;
    } catch (error) {
        console.error("Error fetching companies by state:", error);
        throw error;
    }
};

export const getCompanies = () => {
    return axios
        .get("http://localhost:8080/v1/company")
        .then((response) => response)
        .catch((error) => {
            console.error("Error in API request", error);
            return null; // Return null if the request fails
        });
};
