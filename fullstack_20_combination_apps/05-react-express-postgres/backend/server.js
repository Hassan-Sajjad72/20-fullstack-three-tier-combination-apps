import express from "express";
    import pg from "pg"; const { Client } = pg;
async function checkDb() { const c=new Client({connectionString:process.env.DATABASE_URL,connectionTimeoutMillis:5000}); await c.connect(); await c.query("SELECT 1"); await c.end(); }
    const app=express();
    app.get("/health", async (_req,res)=>{try{await checkDb();res.json({status:"ok",database:"postgresql"})}catch{res.status(503).json({status:"error"})}});
    app.get("/api/v2/message", (_req,res)=>res.json({message:"05-react-express-postgres is working"}));
    app.listen(Number(process.env.PORT||4000), process.env.HOST||"0.0.0.0");
