#!/bin/bash
# writed by J.A NachE <nache.nache@gmail.com>
# under GPL v3

HTKBIN="/opt/bin"

echo "Ejecutando prompts2wlist prompts wlist"
perl prompts2wlist prompts wlist
echo -e "SENT-END\nSENT-START" >> wlist



echo "Creando global.ded"
echo -ee "AS sp\nRS cmu\nMP sil sil sp" >global.ded 

echo "Generando un diccionario propio"
python makelexicon.py > lexicon.tmp

echo "generando dict y monophones1"
$HTKBIN/HDMan -A -D -T 1 -m -w wlist -n monophones1 -i -l dlog dict lexicon.tmp
echo "sil" >> monophones1
echo "SENT-END             [SENT-END]           sil" >>dict


echo "generando monophones0"
cat monophones1 | grep -v ^sp >monophones0
#echo "sil" >> monophones0


rm -rf train
mkdir train
mkdir train/wav

read -p "ahora vamos a grabar el contenido de prompts. tienes 3 segundos para decir cada frase. presiona enter para empzar"
while read line; do

    archivo=`echo $line | cut -d " " -f1 | cut -d "/" -f 2`
    texto=`echo $line | cut -d " " -f2-`
    echo "Di esto: $texto"
    arecord -f S16_LE -r 48000 -d 3 train/wav/$archivo.wav 

done < prompts


echo "pasando de prompts a words.mlf (prompts2mlf)"
perl prompts2mlf words.mlf prompts


echo "Generando el archivo mkphones0.led"
echo -e "EX\nIS sil sil\nDE sp" >mkphones0.led

echo "Generando phones0.mlf"
$HTKBIN/HLEd -A -D -T 1 -l '*' -d dict -i phones0.mlf mkphones0.led words.mlf 

echo "generando mkphones1.led"
echo -e "EX\nIS sil sil" >mkphones1.led



echo "Generando phones1.mlf"
$HTKBIN/HLEd -A -D -T 1 -l '*' -d dict -i phones1.mlf mkphones1.led words.mlf 


echo "Generando el archivo codetrain.scp"
rm codetrain.scp
mkdir train/mfcc 2>/dev/null
for file in train/wav/*
do
e=`echo $file | sed s/'\.wav'/'\.mfc'/g | sed s/'\/wav\/'/'\/mfcc\/'/g`
echo "$file $e" >>codetrain.scp
done

echo "creando el archivo wav_config"
echo -e "SOURCEFORMAT = WAV\nTARGETKIND = MFCC_0_D\nTARGETRATE = 100000.0\nSAVECOMPRESSED = T\nSAVEWITHCRC = T\nWINDOWSIZE = 250000.0\nUSEHAMMING = T\nPREEMCOEF = 0.97\nNUMCHANS = 26\nCEPLIFTER = 22\nNUMCEPS = 12" > wav_config


echo "Comenzando la codificacion de los .wav en mfc con HCopy"
$HTKBIN/HCopy -A -D -T 1 -C wav_config -S codetrain.scp


echo "Creando el archivo proto"
echo -e "~o <VecSize> 25 <MFCC_0_D_N_Z>\n~h "proto"\n<BeginHMM>\n  <NumStates> 5\n  <State> 2\n    <Mean> 25\n      0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n    <Variance> 25\n      1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0\n <State> 3\n    <Mean> 25\n      0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n    <Variance> 25\n      1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0\n <State> 4\n    <Mean> 25\n      0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n    <Variance> 25\n      1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0\n <TransP> 5\n  0.0 1.0 0.0 0.0 0.0\n  0.0 0.6 0.4 0.0 0.0\n  0.0 0.0 0.6 0.4 0.0\n  0.0 0.0 0.0 0.7 0.3\n  0.0 0.0 0.0 0.0 0.0\n<EndHMM>" >proto


echo "creando el archivo config"
echo -e "TARGETKIND = MFCC_0_D_N_Z\nTARGETRATE = 100000.0\nSAVECOMPRESSED = T\nSAVEWITHCRC = T\nWINDOWSIZE = 250000.0\nUSEHAMMING = T\nPREEMCOEF = 0.97\nNUMCHANS = 26\nCEPLIFTER = 22\nNUMCEPS = 12" >config


echo "creando el archivo train.scp"
rm -rf train.scp

for file in train/mfcc/*
do
 echo "$file" >> train.scp
done

echo "borrando y creando directorio hmm0"
rm -rf hmm0
mkdir hmm0

echo "Ejecutando HCompV (creando archivo hmm0/proto y hmm0/vFloors"
$HTKBIN/HCompV -A -D -T 1 -C config -f 0.01 -m -S train.scp -M hmm0 proto

echo "Creando el archivo hmm0/hmmdefs"
rm hmm0/hmmdefs
cat hmm0/proto | grep -v "~o" | grep -v "VECSIZE" | grep -v "~h" | grep -v "STREAMINFO" > hmm0/proto_nache_trunked
while read line; do 
    echo "~h \"$line\"" >> hmm0/hmmdefs
    cat hmm0/proto_nache_trunked >> hmm0/hmmdefs
done < monophones0
echo -e "\n" >> hmm0/hmmdefs

echo "creando el archivo hmm0/macros"
head -n 3 hmm0/proto > hmm0/macros
cat hmm0/vFloors >> hmm0/macros


echo "Creando directorios desde hmm1 hasta hmm9"
rm -rf hmm1
rm -rf hmm2
rm -rf hmm3
rm -rf hmm4
rm -rf hmm5
rm -rf hmm6
rm -rf hmm7
rm -rf hmm8
rm -rf hmm9
mkdir hmm1
mkdir hmm2
mkdir hmm3
mkdir hmm4
mkdir hmm5
mkdir hmm6
mkdir hmm7
mkdir hmm8
mkdir hmm9

echo "Reestimando 1..."
$HTKBIN/HERest -A -D -T 1 -C config -I phones0.mlf -t 250.0 150.0 1000.0 -S train.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 monophones0

echo "Reestimando 2..."
$HTKBIN/HERest -A -D -T 1 -C config -I phones0.mlf -t 250.0 150.0 1000.0 -S train.scp -H hmm1/macros -H hmm1/hmmdefs -M hmm2 monophones0

echo "Reestimando 3..."
$HTKBIN/HERest -A -D -T 1 -C config -I phones0.mlf -t 250.0 150.0 1000.0 -S train.scp -H hmm2/macros -H hmm2/hmmdefs -M hmm3 monophones0


echo "Aniadiendo el modelo sp en hmm4"
cp -r hmm3/* hmm4/
tail -n 28 hmm4/hmmdefs > hmm4/hmA.tmp
echo -e "~h \"sp\"\n<BEGINHMM>\n<NUMSTATES> 3\n<STATE> 2" > hmm4/hmB.tmp
cat hmm4/hmA.tmp | tail -n 18 | head -n 5 >> hmm4/hmB.tmp
echo -e "<TRANSP> 3\n 0.0 1.0 0.0\n 0.0 0.9 0.1\n 0.0 0.0 0.0\n<ENDHMM>" >>hmm4/hmB.tmp
cat hmm4/hmB.tmp >> hmm4/hmmdefs


echo "Creando el archivo sil.hed"
echo -e "AT 2 4 0.2 {sil.transP}\nAT 4 2 0.2 {sil.transP}\nAT 1 3 0.3 {sp.transP}\nTI silst {sil.state[3],sp.state[2]}" >sil.hed

echo "Ejecutando HHEd y dos HERest"
$HTKBIN/HHEd -A -D -T 1 -H hmm4/macros -H hmm4/hmmdefs -M hmm5 sil.hed monophones1
$HTKBIN/HERest -A -D -T 1 -C config  -I phones1.mlf -t 250.0 150.0 3000.0 -S train.scp -H hmm5/macros -H  hmm5/hmmdefs -M hmm6 monophones1
$HTKBIN/HERest -A -D -T 1 -C config  -I phones1.mlf -t 250.0 150.0 3000.0 -S train.scp -H hmm6/macros -H hmm6/hmmdefs -M hmm7 monophones1

$HTKBIN/HVite -A -D -T 1 -l '*' -o SWT -b SENT-END -C config -H hmm7/macros -H hmm7/hmmdefs -i aligned.mlf -m -t 250.0 150.0 1000.0 -y lab -a -I words.mlf -S train.scp dict monophones1> HVite_log
$HTKBIN/HERest -A -D -T 1 -C config -I aligned.mlf -t 250.0 150.0 3000.0 -S train.scp -H hmm7/macros -H hmm7/hmmdefs -M hmm8 monophones1 
$HTKBIN/HERest -A -D -T 1 -C config -I aligned.mlf -t 250.0 150.0 3000.0 -S train.scp -H hmm8/macros -H hmm8/hmmdefs -M hmm9 monophones1


