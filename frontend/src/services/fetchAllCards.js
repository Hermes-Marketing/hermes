export const fetchAllCards = async () => {
  const apiUrl = import.meta.env.VITE_API_URL;
  try {
    const response = await fetch(`${apiUrl}/v1/company/`, {
      mode: "no-cors", // Will need to change
    });
    if (response.ok) {
      // Check if the response is JSON before parsing
      const contentType = response.headers.get("Content-Type");
      if (contentType && contentType.includes("application/json")) {
        const data = await response.json();
        console.log("Success:", data);
        return data;
      } else {
        console.error(
          "Failed to fetch cards: Not JSON response. Response type:",
          contentType
        );
        return null;
      }
    } else {
      console.error("Failed to fetch cards:", response.status);
      return null;
    }
  } catch (error) {
    console.error("Error fetching cards:", error);
    return null;
  }
};
