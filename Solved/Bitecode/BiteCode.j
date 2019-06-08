.version 45 0 
.class public BiteCode 
.super java/lang/Object 
.field private static synthetic a I 

.method public static main : ([Ljava/lang/String;)V 
    .code stack 10 locals 5 
L0:     ldc 'Stuck? Maybe try Krakatau!' 
L2:     pop 
L3:     getstatic Field BiteCode a I 
L6:     aload_0 
L7:     arraylength 
L8:     istore_1 
L9:     istore_2 
L10:    iload_1 
L11:    iconst_1 
L12:    isub 
L13:    ifeq L19 
L16:    jsr L51 
L19:    jsr L22 
L22:    jsr L25 
L25:    pop2 
L26:    aload_0 
L27:    iconst_0 
L28:    aaload 
L29:    invokevirtual Method java/lang/String toCharArray ()[C 
L32:    dup 
L33:    astore_3 
L34:    arraylength 
L35:    istore 4 
L37:    iload 4 
L39:    ldc 927739485 
L41:    ixor 
L42:    ldc 927739457 
L44:    ixor 
L45:    ifeq L85 
L48:    jsr L51 
L51:    aconst_null 
L52:    checkcast '\x00java/lang/System' 
L55:    pop2 
L56:    getstatic Field java/lang/System out Ljava/io/PrintStream; 
L59:    ldc 'Nah' 
L61:    invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
L64:    return 
L65:    iload_2 
L66:    lookupswitch 
            default : L76 

L76:    getstatic Field java/lang/System out Ljava/io/PrintStream; 
L79:    ldc 'Yeah' 
L81:    invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
L84:    return 
L85:    aload_3 
L86:    dup 
L87:    iconst_0 
L88:    caload 
L89:    ldc 189074585 
L91:    ixor 
L92:    ldc 189074673 
L94:    isub 
L95:    ifeq L106 
L98:    pop 
L99:    iload_2 
L100:   ifne L535 
L103:   jsr L51 
L106:   dup 
L107:   iconst_1 
L108:   caload 
L109:   ldc -227215135 
L111:   ixor 
L112:   ldc -227215214 
L114:   isub 
L115:   ifeq L126 
L118:   pop 
L119:   iload_2 
L120:   ifne L179 
L123:   jsr L51 
L126:   dup 
L127:   iconst_2 
L128:   caload 
L129:   ldc 19240864 
L131:   ixor 
L132:   ldc 19240899 
L134:   isub 
L135:   ifeq L146 
L138:   pop 
L139:   iload_2 
L140:   ifne L99 
L143:   jsr L51 
L146:   dup 
L147:   iconst_3 
L148:   caload 
L149:   ldc 245881291 
L151:   ixor 
L152:   ldc 245881279 
L154:   isub 
L155:   ifeq L166 
L158:   pop 
L159:   iload_2 
L160:   ifne L409 
L163:   jsr L51 
L166:   dup 
L167:   iconst_4 
L168:   caload 
L169:   ldc 233391094 
L171:   ixor 
L172:   ldc 233390992 
L174:   isub 
L175:   ifeq L186 
L178:   pop 
L179:   iload_2 
L180:   ifne L388 
L183:   jsr L51 
L186:   dup 
L187:   iconst_5 
L188:   caload 
L189:   ldc 56978353 
L191:   ixor 
L192:   ldc 56978378 
L194:   isub 
L195:   ifeq L206 
L198:   pop 
L199:   iload_2 
L200:   ifne L346 
L203:   jsr L51 
L206:   dup 
L207:   bipush 6 
L209:   caload 
L210:   ldc -213838484 
L212:   ixor 
L213:   ldc -213838565 
L215:   isub 
L216:   ifeq L227 
L219:   pop 
L220:   iload_2 
L221:   ifne L367 
L224:   jsr L51 
L227:   dup 
L228:   bipush 7 
L230:   caload 
L231:   ldc -231671677 
L233:   ixor 
L234:   ldc -231671605 
L236:   isub 
L237:   ifeq L248 
L240:   pop 
L241:   iload_2 
L242:   ifne L220 
L245:   jsr L51 
L248:   dup 
L249:   bipush 8 
L251:   caload 
L252:   ldc -132473862 
L254:   ixor 
L255:   ldc -132473910 
L257:   isub 
L258:   ifeq L269 
L261:   pop 
L262:   iload_2 
L263:   ifne L640 
L266:   jsr L51 
L269:   dup 
L270:   bipush 9 
L272:   caload 
L273:   ldc 143449065 
L275:   ixor 
L276:   ldc 143449053 
L278:   isub 
L279:   ifeq L290 
L282:   pop 
L283:   iload_2 
L284:   ifne L367 
L287:   jsr L51 
L290:   dup 
L291:   bipush 10 
L293:   caload 
L294:   ldc 108102484 
L296:   ixor 
L297:   ldc 108102411 
L299:   isub 
L300:   ifeq L311 
L303:   pop 
L304:   iload_2 
L305:   ifne L220 
L308:   jsr L51 
L311:   dup 
L312:   bipush 11 
L314:   caload 
L315:   ldc 71123188 
L317:   ixor 
L318:   ldc 71123073 
L320:   isub 
L321:   ifeq L332 
L324:   pop 
L325:   iload_2 
L326:   ifne L199 
L329:   jsr L51 
L332:   dup 
L333:   bipush 12 
L335:   caload 
L336:   ldc 146096006 
L338:   ixor 
L339:   ldc 146096089 
L341:   isub 
L342:   ifeq L353 
L345:   pop 
L346:   iload_2 
L347:   ifne L283 
L350:   jsr L51 
L353:   dup 
L354:   bipush 13 
L356:   caload 
L357:   ldc -173487738 
L359:   ixor 
L360:   ldc -173487628 
L362:   isub 
L363:   ifeq L374 
L366:   pop 
L367:   iload_2 
L368:   ifne L179 
L371:   jsr L51 
L374:   dup 
L375:   bipush 14 
L377:   caload 
L378:   ldc -116507045 
L380:   ixor 
L381:   ldc -116507132 
L383:   isub 
L384:   ifeq L395 
L387:   pop 
L388:   iload_2 
L389:   ifne L472 
L392:   jsr L51 
L395:   dup 
L396:   bipush 15 
L398:   caload 
L399:   ldc -68013365 
L401:   ixor 
L402:   ldc -68013319 
L404:   isub 
L405:   ifeq L416 
L408:   pop 
L409:   iload_2 
L410:   ifne L493 
L413:   jsr L51 
L416:   dup 
L417:   bipush 16 
L419:   caload 
L420:   ldc 171414622 
L422:   ixor 
L423:   ldc 171414529 
L425:   isub 
L426:   ifeq L437 
L429:   pop 
L430:   iload_2 
L431:   ifne L304 
L434:   jsr L51 
L437:   dup 
L438:   bipush 17 
L440:   caload 
L441:   ldc 94412444 
L443:   ixor 
L444:   ldc 94412524 
L446:   isub 
L447:   ifeq L458 
L450:   pop 
L451:   iload_2 
L452:   ifne L556 
L455:   jsr L51 
L458:   dup 
L459:   bipush 18 
L461:   caload 
L462:   ldc 197453081 
L464:   ixor 
L465:   ldc 197453163 
L467:   isub 
L468:   ifeq L479 
L471:   pop 
L472:   iload_2 
L473:   ifne L119 
L476:   jsr L51 
L479:   dup 
L480:   bipush 19 
L482:   caload 
L483:   ldc -50622153 
L485:   ixor 
L486:   ldc -50622201 
L488:   isub 
L489:   ifeq L500 
L492:   pop 
L493:   iload_2 
L494:   ifne L451 
L497:   jsr L51 
L500:   dup 
L501:   bipush 20 
L503:   caload 
L504:   ldc 190140381 
L506:   ixor 
L507:   ldc 190140290 
L509:   isub 
L510:   ifeq L521 
L513:   pop 
L514:   iload_2 
L515:   ifne L241 
L518:   jsr L51 
L521:   dup 
L522:   bipush 21 
L524:   caload 
L525:   ldc 77383944 
L527:   ixor 
L528:   ldc 77383996 
L530:   isub 
L531:   ifeq L542 
L534:   pop 
L535:   iload_2 
L536:   ifne L220 
L539:   jsr L51 
L542:   dup 
L543:   bipush 22 
L545:   caload 
L546:   ldc -41590082 
L548:   ixor 
L549:   ldc -41590047 
L551:   isub 
L552:   ifeq L563 
L555:   pop 
L556:   iload_2 
L557:   ifne L409 
L560:   jsr L51 
L563:   dup 
L564:   bipush 23 
L566:   caload 
L567:   ldc 61204303 
L569:   ixor 
L570:   ldc 61204283 
L572:   isub 
L573:   ifeq L584 
L576:   pop 
L577:   iload_2 
L578:   ifne L430 
L581:   jsr L51 
L584:   dup 
L585:   bipush 24 
L587:   caload 
L588:   ldc -24637751 
L590:   ixor 
L591:   ldc -24637791 
L593:   isub 
L594:   ifeq L605 
L597:   pop 
L598:   iload_2 
L599:   ifne L241 
L602:   jsr L51 
L605:   dup 
L606:   bipush 25 
L608:   caload 
L609:   ldc 61697107 
L611:   ixor 
L612:   ldc 61697122 
L614:   isub 
L615:   ifeq L626 
L618:   pop 
L619:   iload_2 
L620:   ifne L99 
L623:   jsr L51 
L626:   dup 
L627:   bipush 26 
L629:   caload 
L630:   ldc 267894989 
L632:   ixor 
L633:   ldc 267895017 
L635:   isub 
L636:   ifeq L647 
L639:   pop 
L640:   iload_2 
L641:   ifne L640 
L644:   jsr L51 
L647:   dup 
L648:   bipush 27 
L650:   caload 
L651:   ldc -13480562 
L653:   ixor 
L654:   ldc -13480461 
L656:   isub 
L657:   ifeq L65 
L660:   pop 
L661:   iload_2 
L662:   ifne L577 
L665:   jsr L51 
L668:   return 
L669:   
    .end code 
.end method 
.end class 
