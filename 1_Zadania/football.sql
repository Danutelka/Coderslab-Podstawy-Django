--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.9
-- Dumped by pg_dump version 9.5.9

-- Started on 2017-10-17 15:28:25 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 12395)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2164 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- TOC entry 1 (class 3079 OID 16395)
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- TOC entry 2165 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 185 (class 1259 OID 16624)
-- Name: games; Type: TABLE; Schema: public; Owner: pawel
--

CREATE TABLE games (
    id bigint NOT NULL,
    team_home bigint,
    team_home_goals bigint,
    team_away bigint,
    team_away_goals bigint
);


--
-- TOC entry 184 (class 1259 OID 16622)
-- Name: games_id_seq; Type: SEQUENCE; Schema: public; Owner: pawel
--

CREATE SEQUENCE games_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2166 (class 0 OID 0)
-- Dependencies: 184
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pawel
--

ALTER SEQUENCE games_id_seq OWNED BY games.id;


--
-- TOC entry 187 (class 1259 OID 16630)
-- Name: teams; Type: TABLE; Schema: public; Owner: pawel
--

CREATE TABLE teams (
    id bigint NOT NULL,
    name text NOT NULL,
    points bigint
);


--
-- TOC entry 186 (class 1259 OID 16628)
-- Name: teams_id_seq; Type: SEQUENCE; Schema: public; Owner: pawel
--

CREATE SEQUENCE teams_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2167 (class 0 OID 0)
-- Dependencies: 186
-- Name: teams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pawel
--

ALTER SEQUENCE teams_id_seq OWNED BY teams.id;


--
-- TOC entry 2029 (class 2604 OID 16627)
-- Name: id; Type: DEFAULT; Schema: public; Owner: pawel
--

ALTER TABLE ONLY games ALTER COLUMN id SET DEFAULT nextval('games_id_seq'::regclass);


--
-- TOC entry 2030 (class 2604 OID 16633)
-- Name: id; Type: DEFAULT; Schema: public; Owner: pawel
--

ALTER TABLE ONLY teams ALTER COLUMN id SET DEFAULT nextval('teams_id_seq'::regclass);


--
-- TOC entry 2154 (class 0 OID 16624)
-- Dependencies: 185
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: pawel
--

INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (17, 1, 0, 4, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (18, 1, 1, 5, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (19, 1, 3, 6, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (20, 1, 5, 8, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (21, 1, 1, 9, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (22, 1, 1, 10, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (23, 1, 3, 14, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (24, 1, 3, 16, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (25, 2, 2, 1, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (26, 2, 2, 4, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (27, 2, 2, 5, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (28, 2, 0, 6, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (29, 2, 2, 9, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (30, 2, 2, 14, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (31, 2, 5, 16, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (32, 3, 1, 1, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (33, 3, 1, 2, 5);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (34, 3, 1, 4, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (35, 3, 3, 7, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (36, 3, 4, 12, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (37, 3, 5, 16, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (38, 4, 0, 5, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (39, 4, 2, 6, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (40, 4, 1, 7, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (41, 4, 4, 9, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (42, 4, 2, 11, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (43, 4, 1, 14, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (44, 4, 4, 15, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (48, 5, 1, 3, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (49, 5, 0, 7, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (50, 5, 2, 8, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (51, 5, 3, 9, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (52, 5, 0, 10, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (53, 5, 1, 11, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (54, 5, 2, 15, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (55, 6, 2, 3, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (56, 6, 1, 5, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (57, 6, 1, 8, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (58, 6, 0, 9, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (59, 6, 2, 10, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (60, 6, 1, 11, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (61, 6, 4, 13, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (62, 6, 4, 14, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (63, 7, 1, 1, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (64, 7, 0, 2, 4);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (65, 7, 1, 6, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (66, 7, 1, 11, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (67, 7, 2, 12, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (68, 7, 1, 14, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (69, 7, 0, 16, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (70, 8, 0, 3, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (71, 8, 0, 4, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (72, 8, 0, 7, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (73, 8, 1, 10, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (74, 8, 0, 11, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (75, 8, 2, 12, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (76, 8, 3, 13, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (77, 8, 5, 15, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (78, 9, 2, 3, 5);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (79, 9, 0, 7, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (80, 9, 1, 8, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (81, 9, 2, 10, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (82, 9, 1, 11, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (83, 9, 4, 13, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (84, 9, 4, 15, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (85, 10, 0, 2, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (86, 10, 1, 3, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (87, 10, 2, 4, 6);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (88, 10, 3, 7, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (89, 10, 2, 11, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (90, 10, 1, 12, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (91, 10, 2, 13, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (92, 10, 0, 15, 4);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (93, 11, 2, 1, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (94, 11, 1, 2, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (95, 11, 0, 5, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (96, 11, 5, 12, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (97, 11, 2, 14, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (98, 11, 3, 16, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (99, 12, 1, 1, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (100, 12, 1, 2, 5);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (101, 12, 2, 4, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (102, 12, 1, 5, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (103, 12, 0, 6, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (104, 12, 0, 9, 5);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (105, 12, 3, 14, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (106, 12, 2, 16, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (107, 13, 1, 1, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (108, 13, 0, 2, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (109, 13, 1, 4, 5);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (110, 13, 0, 7, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (111, 13, 2, 11, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (112, 13, 2, 12, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (113, 13, 1, 15, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (114, 13, 3, 16, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (115, 14, 0, 3, 5);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (116, 14, 2, 5, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (117, 14, 2, 8, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (118, 14, 1, 9, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (119, 14, 2, 10, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (120, 14, 1, 13, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (121, 14, 3, 15, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (122, 15, 0, 1, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (123, 15, 1, 2, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (124, 15, 1, 6, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (125, 15, 0, 7, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (126, 15, 3, 11, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (127, 15, 1, 12, 4);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (128, 15, 2, 16, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (129, 16, 1, 3, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (130, 16, 0, 4, 2);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (131, 16, 0, 5, 4);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (132, 16, 1, 6, 4);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (133, 16, 1, 8, 3);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (134, 16, 3, 9, 0);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (135, 16, 2, 10, 1);
INSERT INTO public.games (id, team_home, team_home_goals, team_away, team_away_goals) VALUES (136, 16, 4, 14, 0);



--
-- TOC entry 2168 (class 0 OID 0)
-- Dependencies: 184
-- Name: games_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pawel
--

SELECT pg_catalog.setval('games_id_seq', 136, true);


--
-- TOC entry 2156 (class 0 OID 16630)
-- Dependencies: 187
-- Data for Name: teams; Type: TABLE DATA; Schema: public; Owner: pawel
--

INSERT INTO public.teams (id, name, points) VALUES (1, 'Piast Piastów', 37);
INSERT INTO public.teams (id, name, points) VALUES (2, 'Perła Złotokłos', 34);
INSERT INTO public.teams (id, name, points) VALUES (3, 'LKS Chlebnia', 34);
INSERT INTO public.teams (id, name, points) VALUES (4, 'Naprzód Brwinów', 28);
INSERT INTO public.teams (id, name, points) VALUES (5, 'KS Teresin', 26);
INSERT INTO public.teams (id, name, points) VALUES (6, 'Józefovia Józefów', 20);
INSERT INTO public.teams (id, name, points) VALUES (7, 'Okęcie Warszawa', 19);
INSERT INTO public.teams (id, name, points) VALUES (8, 'Żyrardowianka Żyrardów', 18);
INSERT INTO public.teams (id, name, points) VALUES (9, 'Przyszłość Włochy', 18);
INSERT INTO public.teams (id, name, points) VALUES (10, 'Ryś Laski', 17);
INSERT INTO public.teams (id, name, points) VALUES (11, 'SEMP Ursynów', 17);
INSERT INTO public.teams (id, name, points) VALUES (12, 'Promyk Nowa Sucha', 15);
INSERT INTO public.teams (id, name, points) VALUES (13, 'Świt Warszawa', 13);
INSERT INTO public.teams (id, name, points) VALUES (14, 'FC Lesznowola', 12);
INSERT INTO public.teams (id, name, points) VALUES (15, 'Pogoń II Grodzisk Mazowiecki', 12);
INSERT INTO public.teams (id, name, points) VALUES (16, 'Milan Milanówek', 12);


--
-- TOC entry 2169 (class 0 OID 0)
-- Dependencies: 186
-- Name: teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pawel
--

SELECT pg_catalog.setval('teams_id_seq', 16, true);


--
-- TOC entry 2034 (class 2606 OID 16646)
-- Name: idx_16624_primary; Type: CONSTRAINT; Schema: public; Owner: pawel
--

ALTER TABLE ONLY games
    ADD CONSTRAINT idx_16624_primary PRIMARY KEY (id);


--
-- TOC entry 2036 (class 2606 OID 16647)
-- Name: idx_16630_primary; Type: CONSTRAINT; Schema: public; Owner: pawel
--

ALTER TABLE ONLY teams
    ADD CONSTRAINT idx_16630_primary PRIMARY KEY (id);


--
-- TOC entry 2031 (class 1259 OID 16638)
-- Name: idx_16624_fk_games_1_idx; Type: INDEX; Schema: public; Owner: pawel
--

CREATE INDEX idx_16624_fk_games_1_idx ON games USING btree (team_home);


--
-- TOC entry 2032 (class 1259 OID 16637)
-- Name: idx_16624_fk_games_2_idx; Type: INDEX; Schema: public; Owner: pawel
--

CREATE INDEX idx_16624_fk_games_2_idx ON games USING btree (team_away);


--
-- TOC entry 2037 (class 2606 OID 16648)
-- Name: fk_games_1; Type: FK CONSTRAINT; Schema: public; Owner: pawel
--

ALTER TABLE ONLY games
    ADD CONSTRAINT fk_games_1 FOREIGN KEY (team_home) REFERENCES teams(id);


--
-- TOC entry 2038 (class 2606 OID 16653)
-- Name: fk_games_2; Type: FK CONSTRAINT; Schema: public; Owner: pawel
--

ALTER TABLE ONLY games
    ADD CONSTRAINT fk_games_2 FOREIGN KEY (team_away) REFERENCES teams(id);


--
-- TOC entry 2163 (class 0 OID 0)
-- Dependencies: 7
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2017-10-17 15:28:25 CEST

--
-- PostgreSQL database dump complete
--

