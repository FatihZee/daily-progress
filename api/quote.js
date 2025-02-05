export default async function handler(req, res) {
    try {
        const API_URL = "https://api.api-ninjas.com/v1/quotes";
        const API_KEY = process.env.API_KEY;

        if (!API_KEY) {
            throw new Error("API_KEY is missing. Set it in Vercel Environment Variables.");
        }

        const response = await fetch(API_URL, {
            headers: { "X-Api-Key": API_KEY }
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }

        const data = await response.json();
        res.status(200).json(data[0]);
    } catch (error) {
        console.error("Error fetching quote:", error.message);
        res.status(500).json({ error: error.message });
    }
}
