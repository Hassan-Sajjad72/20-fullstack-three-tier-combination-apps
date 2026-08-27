import express from "express";
    import mysql from "mysql2/promise";
async function checkDb() { const c=await mysql.createConnection(process.env.DATABASE_URL); await c.query("SELECT 1"); await c.end(); }
    const app=express();
    app.get("/healthz", async (_req,res)=>{try{await checkDb();res.json({status:"ok",database:"mysql"})}catch{res.status(503).json({status:"error"})}});
    app.get("/api/message", (_req,res)=>res.json({message:"14-vue-express-mysql is working"}));
    app.listen(Number(process.env.PORT||4000), process.env.HOST||"0.0.0.0");
